# MQTT LOGGER
Broker based logging application in python.Can be combine to any of your services you want.

#### Example usage
    > python main.py app_name http_servcie
    
    Application initialized with arguments
    
    --------------------Stared Services---------------------------
    Time                 Application                    Service                       
    14:57:13             app_name                       http_service               
    ====================---------------===========================
    
    Subscribing topics...
    Topic subscribed : app_name/http_service/log
    
    APP_NAME/HTTP_SERVICE ==> 14:18:02 : {{ `you can publish any of messsage you want to the topic app_name/http_service/log` }}
    APP_NAME/HTTP_SERVICE ==> 14:18:02 : {{ `you can publish any of messsage you want to the topic app_name/http_service/log` }}
    APP_NAME/HTTP_SERVICE ==> 14:18:02 : {{ `you can publish any of messsage you want to the topic app_name/http_service/log` }}
