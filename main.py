import streamlit as st
#import requests
#import re
#import base64
#from bs4 import BeautifulSoup

class Base64(object):
    CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

    def chunk(self, data, length):
        return [data[i:i+length] for i in range(0, len(data), length)]

    def encode(self, data):
        override = 0
        if len(data) % 3 != 0:
            override = (len(data) + 3 - len(data) % 3) - len(data)
        data += b"\x00"*override

        threechunks = self.chunk(data, 3)

        binstring = ""
        for chunk in threechunks:
            for x in chunk:
                binstring += "{:0>8}".format(bin(x)[2:])

        sixchunks = self.chunk(binstring, 6)

        outstring = ""
        for element in sixchunks:
            outstring += self.CHARS[int(element, 2)]
        
        outstring = outstring[:-override] + "="*override
        return outstring

    def decode(self, data):
        override = data.count("=")
        data = data.replace("=", "A")
        
        binstring = ""
        for char in data:
            binstring += "{:0>6b}".format(self.CHARS.index(char))

        eightchunks = self.chunk(binstring, 8)
        
        outbytes = b""
        for chunk in eightchunks:
            outbytes += bytes([int(chunk, 2)])

        return outbytes[:-override]


b64 = Base64()
def encrypt(text):
    return b64.encode(bytes(text,'utf-8'))

"""
#e_ means encrypted 
def encrypt(text):
    return base64.b64encode(text.encode('utf-8')).decode('utf-8')
"""
#chose 23 or 22
st_year=st.radio("Chose Year",["23","22"])
year='23' if False else '22'
#chose college
st_college_code=st.number_input("Enter college code",100,1000,101)
college_code = '101' if True else str(input("enter your college code:"))
college_roll='004' if True else str(input("enter your college roll:"))
st_college_roll=st.number_input("Enter college roll number",0,2000,1)

if st_college_roll<10:
    st_college_roll='00'+str(st_college_roll)
elif 10<=st_college_roll<=99:
    st_college_roll='0'+str(st_college_roll)
else:
    st_college_roll=str(st_college_roll)

roll_number='4382'+year+college_code +'88' +college_roll+'@@7178'
st_roll_number='4382'+st_year+str(st_college_code)+'88'+st_college_roll+'@@7178'
print(roll_number)
e_roll_number=encrypt(roll_number)
e_st_roll_number=encrypt(st_roll_number)

sem='2'
st_sem=st.radio("Enter semester",['2','4'])
#print(encrypt(sem))
e_sem=encrypt(sem)
e_st_sem=encrypt(st_sem)
#Student Type
s_type='REGULAR' if False else "ATKT"
st_s_type=st.radio("Student Type",["REGULAR","ATKT"])
e_s_type=encrypt(s_type)
e_st_s_type=encrypt(st_s_type)


#Stream
stream="Master of Science in Mathematics"
st_stream=st.radio("Chose stream",["Master of Science in Mathematics"])
e_stream=encrypt(stream)
e_st_stream=encrypt(st_stream)
generated_url="http://www.prsuuniv.in/home/student/result19/"+e_sem+"/"+e_s_type+"/"+e_roll_number+"/"+e_stream
st_generated_url="http://www.prsuuniv.in/home/student/result19/"+e_st_sem+"/"+e_st_s_type+"/"+e_st_roll_number+"/"+e_st_stream

print(generated_url)
button=st.link_button("RESULT",st_generated_url)
st.write(st_generated_url)
