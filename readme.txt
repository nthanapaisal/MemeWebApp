Final Project, Cloud Computing. 

Members:
Supakjeera Thanapaisal
Jonathan Kyle Becker
Bryant Gutierrez
Nuhia Vincent Pham
_____________________________________________________________________________________________________________
Creat env:
    python3 -m venv venv
Activate env:
    Mac:
        source venv/bin/activate
    Windows:
        venv\Scripts\activate

Windows: 
    Install Docker: 
        https://docs.docker.com/docker-for-windows/install/
        install WSL -> pick linux distributor -> change WSL version to 2 -> install docker normally
    before creating virtual env:
        Run shell as Administrator. 
            > Get-ExecutionPolicy
            > Set-ExecutionPolicy remoteSigned
        To Undo
            > Set-ExecutionPolicy restricted    
        
Run locally:
    python3 myapp.py

Run Docker:
    docker-compose up -d
    docker images
    docker ps
    docker ps -a
    docker-compose down