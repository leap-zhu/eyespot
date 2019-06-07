import hashlib

from instafarm import app
from datetime import datetime
from instafarm.models import model
from instafarm.viewset.base import json_response, get_request

@app.route('/apis/admin/signup', methods = ['POST'])
def signup():
    print('admin/signup')
    data = {}
    keys =['email', 'password']
    try: 
        for key in keys:
            data[key] = get_request(key, None)
        
        if model.User.check_exist_by_email(data['email']):
            return json_response({
                "success": False,
                "message": 'This email is alread used by another person.'
            })

        password = hashlib.md5(data['password'].encode()).hexdigest()
        user = model.User(data['email'], password, 1)
        model.add(user)
        model.commit()

        return json_response({
            'success': True,
            'message': 'Sign up success.',
        })
    except:
        return json_response({
            'success': False,
            'message': 'Error occurs. Please try again later.',
        })

