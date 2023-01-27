src="file_system_move_File.py"
destination=""
while True:
    import os
    destination=str(input("What would you like to name this file?")+".py")
    os.rename(src,destination)
    print("source path renamed to detination path successfully.")
    src=destination