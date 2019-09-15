import argparse
import os
import sys

INPUT_FOLDER = 'C:\\Firmware\\PhilipsBDP2600\\Bins\\'
SIZE = 4096
PAD_CHAR = 'FF'

BLOCK_SIZE = {
    '01': 6 * SIZE + 512,
    '02': 1 * SIZE,
    '03': 1 * SIZE,
    '04': 15 * SIZE,
    '05': 16 * SIZE,
    '06': 100 * SIZE + 3072,
    '07': 6 * SIZE,
    '08': 0
}

def get_pad_size(filesize):
  while (filesize > 0):
    filesize -= SIZE
  return filesize * -1;

if __name__ == '__main__':
  
  bootloader_bytes = bytearray()
  
  for filename in os.listdir(INPUT_FOLDER):
    if filename.endswith('.bin'):
      fullname = os.path.join(INPUT_FOLDER,filename)
      
      block_number = filename.split('.')[0]
      
      filesize = os.stat(fullname).st_size
      
      padsize = BLOCK_SIZE[block_number] - filesize
      
      if (padsize < 0):
        padsize = 0
            
      chars = b'\xFF' * padsize
      print ('Add ' + str(padsize) + ' bytes to the file "' + filename + '" (source size ' + str(filesize) + ' bytes)')
      
      with open(fullname, "rb") as f:
        bytes = f.read()
        bootloader_bytes+=bytes + chars
        
  print('Writing bootloader.bin...')
  with open ('bootloader.bin', "wb") as f:
    f.write(bootloader_bytes)
  print('Ready!')
      
        
        