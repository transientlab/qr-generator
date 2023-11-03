import qrcode as qr

# QR code format
version = 11
size = 40
border_size = 4
bg_color = (255,0,255)
code_color = (0,255,0)

# generate qr code
def generate_qr(file_name, data, qr_back_color=bg_color, qr_code_color=code_color, qr_size=size, qr_border=border_size, qr_version=version):
    kuerkod = qr.QRCode(
    version=qr_version,
    error_correction=qr.ERROR_CORRECT_L,
    box_size=qr_size,
    border=qr_border
    )
    kuerkod.add_data(data)
    kuerkod.make(fit=False)
    img = kuerkod.make_image(back_color=qr_back_color, fill_color=qr_code_color)
    img.save(file_name + ".png")

def read_vcard(file):
    vkarta = ""
    with open(file) as file_handle:
        for line in file_handle:
            vkarta += line
    print(vkarta)
    return vkarta

def clear_line(input_string):
    return input_string.replace(" " , "").replace("\t" , "").replace("\n" , "")

# parse list for lines with LINK or VCARD or WIFI
def parse_list(file):
    with open(file) as file_handle:
        for line in file_handle:
            splitline = line.split("|")
            filename = clear_line(splitline[2])
            data = clear_line(splitline[1])
            type = clear_line(splitline[0])
            print(data)
            print(filename)
            # weak distinction between {data of qr} and {type of qr}, 
            if "LINK" in type:
                generate_qr(filename, data)
            elif "WIFI" in type:
                generate_qr(filename, "WIFI:" + data)
            elif "VCARD" in type:
                generate_qr(filename, read_vcard(data))
    
if __name__=="__main__":
    parse_list("input-list.txt")
