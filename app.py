from flask import Flask, request,render_template,jsonify
import flasgger
from flasgger import Swagger


app = Flask(__name__)
Swagger(app)
port = os.environ.get('FLASK_PORT') or 8080
port = int(port)
print(port)


@app.route('/predict', methods=["POST"]) # get request from webpage and predict
def predict():
    # Define Swagger interface and Input 
    """NameMapping Algorithm
    
   Basic Service for Mapping of Manufacturer Names without any paramter options.
   Results with "0" represents possible new names.In this case manual correction is necessary.
   We used the best and evaluated model for this service !
   
   Please type the company name
    ---
    parameters:
      - name      : company_name 
        in        : query
        type      : string
        required  : true
    responses:
        8081:
            description: The output    
    """   
    
    input_request                     = request.args.get("company_name") # 
    
    result = jsonify('Es funktioniert ! Dein Input {}'.format(input_request ))
 
    ### ----------------------------------- in case of no parameters ------------------------

    return result

if __name__ == '__main__':
   app.run(port=port,host='0.0.0.0')