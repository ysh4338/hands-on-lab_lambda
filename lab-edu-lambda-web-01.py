import json

def lambda_handler(event, context):
    response = {
        "statusCode": 200,
        "statusDescription": "200 OK",
        "Access-Control-Allow-Origin" : "*",
        "isBase64Encoded": False,
        "headers": {
            "Content-Type": "text/html; charset=utf-8"
        }
    }

    response['body'] = """<html>
    <head>
    <meta charset="utf-8" name="viewport" content="width=device-width, height=device-height, minimum-scale=1.0, maximum-scale=1.0, initial-scale=1.0">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <title>Hello World!</title>
    <style>
        #title {
            font-family: arial; font-size: 2em;color: #eb971a; margin-top:50px;
            text-align: center;
        }
        button {
                background-color: #eb971a;
                border:none;
                color:white;
                border-radius: 5px;
                width:40%;
                height:35px;
                font-size: 13pt;
                margin-top:30px;
                text-align: center;
        }
        #sentence {
                font-size: 17pt;
                margin-top:30px;
                font-weight: bold;
                color: #eb971a;
        }
    </style>
        </head>
        <body>
            <p id="title">Hello World From <b>Lambda</b></p>
            <center><img src="https://velog.velcdn.com/images/chrishan/post/9a9b135f-27a4-49b0-a512-dfa2cbf5d671/image.png" alt="Lambda image" width="500" height="300" align="center" border="0"></center>
            <hr id="lambda-line" width="800px" align="center" color="#eb971a;">
            <center><button onclick="checkEvent();">Who are you?</button></center>
            <center><div id="sentence"></div></center>
        </body>
        <script type="text/javascript">
        
            function checkEvent(){
                $.ajax({ type: "GET", 
                        url: "https://hm3xondha0.execute-api.ap-northeast-2.amazonaws.com/dev", 
                        dataType:'json',
                        success: function(data){ 
                        document.getElementById('sentence').innerHTML = data.status + "&nbsp;&nbsp;" + data.name
                        }, 
                        error: function (error){
                        alert('ERROR::');
                        console.log(error)
                        }

                });
            }

        </script>
        </html>
            
        """
        
    return response