import os

def read_apache_log(log_path):
    if not os.path.exists(log_path):
        print(f"Log file does not exist: {log_path}")
        return

    with open(log_path, 'r') as log_file:
        for line in log_file:
            print(line.strip())

if __name__ == "__main__":
    access_log_path = "/var/log/apache2/access.log"
    print("================== access.log ======================")
    read_apache_log(access_log_path)
    print()
    print()
    error_log_path = "/var/log/apache2/error.log"
    print("================== error.log ======================")
    read_apache_log(error_log_path)
    print()
    print()
    other_vhosts_access_log_path = "/var/log/apache2/other_vhosts_access.log"
    print("================== other_vhosts_access.log ======================")
    read_apache_log(other_vhosts_access_log_path)