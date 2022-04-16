import os

API_ID = int(os.getenv("API_ID", "18891187"))
API_HASH = os.getenv("API_HASH", "7d120384f48b2a86fa2b9e9772a28af6")
BOT_TOKEN = os.getenv("BOT_TOKEN", "5219376297:AAFydXWjPg47TlZ4QnVkc2egji4mPMq0_2w")
SESSION_NAME = os.getenv("SESSION_NAME", "AQB0bx5Nkk_mdot8m0fbfcRxh0gSdBa9oBSgxObY8wwA_fp6h6H0EhjIe6KTWwzg0q7FTcQmIpdkbTcTr9t_zuiqJ9g3GzE2oGdkfdwwqNLR4y3sWFDHT089AdDP4ZRd11kNzaXL-XoH-0VY1GWphQpLippaSz37Q9wRuEuWLVMxTqTkke7z8MTDobAVSH0gDRj5yz-y8nL0lrOJGup9f4JFHCEQfWI4U7hJWoosQ8KJ0cN7afqC5plix2Wrmp9ZYbrqsnCO4Piozo720jSUzIbmkshW4YfIP9XB8Q12Rj4jgZDqfXS4DRxylynGkX2ba0FYvGeZr7rQ3cndM2JJjyeOAAAAASrSOD0A")
COMMAND_PREFIXES = os.getenv("COMMAND_PREFIXES", "!")
BOTLOG_CHATID = os.getenv("BOTLOG_CHATID", "-1001614376277")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://hydra92074:hydra92074@cluster0.ktfkf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
REST_API = os.getenv("REST_API")
SUDO_USERS = list(map(int, os.getenv("SUDO_USERS", "5013387325 784589736").split()))
