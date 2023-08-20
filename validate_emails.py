from re import compile, fullmatch
import dns.resolver as resolver
import threading

approved_domains = []
lock = threading.Lock()

def validate_regex(email):
    regex = compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    return fullmatch(regex, email) is not None

def validate_mx(domain):
    try:
        mail_servers = resolver.resolve(domain, 'MX')
        return True
    except:
        return False

def validate_email(email, result_file):
    if validate_regex(email) :
        _, domain = email.split('@')
        if domain in approved_domains:
            with lock:
                with open(result_file, 'a') as f:
                    f.write(email + '\n')
                    print(f"VALID: {email}")
                    return True
        else:
            if validate_mx(domain):
                with lock:
                    with open(result_file, 'a') as f:
                        f.write(email + '\n')
                        approved_domains.append(domain)
                        print(f"VALID: {email}")
                        return True
            else:
                print(f"INVALID: {email}")
                return False
    print(f"INVALID: {email}")
    return False

def validate_emails_multithreaded(emails, num_threads, result_file):
    def validate_worker(email):
        validate_email(email, result_file)
    
    threads = []
    for email in emails:
        thread = threading.Thread(target=validate_worker, args=(email,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    num_threads = int(input("Enter threads number (use with caution!): "))
    input_file = input("Enter emails file path: ")
    
    email_list = []
    with open(input_file, 'r') as f:
        email_list = [line.strip() for line in f if line.strip()]
    
    result_file = "valid_emails.txt"
    
    validate_emails_multithreaded(email_list, num_threads, result_file)
