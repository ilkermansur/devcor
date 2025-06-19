from netmiko import ConnectHandler

def send_command(host, username, password, command):
    try:
        device_info = {
            "device_type":"cisco_xe",
            "host":host,
            "username":username,
            "password":password,
        }

        conn = ConnectHandler(**device_info)
        output = conn.send_command(command)
        return output

    except:
        return "Tekrar Kontrol Edin, Bir hata"
    
