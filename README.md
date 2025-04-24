# TTM4115
Repository for the TTM4115 project of team 17

## Setup
1. Clone the repository
```bash
git clone https://github.com/OskarLR/TTM4115-Project.git
cd TTM4115-Project
```

2. Install the required packages
```bash
pip install -r requirements.txt
```
3. Change the API URLs in the mobile_client.py file and the main.py file to point to where you run the servers.

4. Start the servers in different terminals

```bash
fastapi dev main.py
```
```bash
fastapi dev scooter_server.py
```

5. Run the mobile client
```bash
streamlit run mobile_client.py
```


`
