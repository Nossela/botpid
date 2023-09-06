from os import getpid

if __name__ == '__main__':
    
    try:
        
        def log_pid(**kwargs) -> None:
            
            with open(kwargs["log_file"], "w") as file:
                file.write(f"get-Process -ID {kwargs['pid']}\n")
                file.write(f"Stop-Process -ID {kwargs['pid']} -Force\n")
                 
        log_pid(log_file="log_file", pid=getpid())
    
    except Exception as e:
        print(e) 
    
    
   
    
            
        def animais(txt):
           
            txt('Elefante')
            
            print(txt)
            
                
             
                
               
             
    