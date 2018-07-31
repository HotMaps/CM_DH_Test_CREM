
#CELERY_BROKER_URL = 'amqp://admin:mypass@rabbit:5672/'
CELERY_BROKER_URL = 'amqp://localhost/'


#CELERY_BROKER_URL = 'amqp://admin:mypass@localhost:5672/'


CM_NAME = 'calculation_module_DH'

RPC_Q = 'rpc_queue_CM' # Do no change this value
CM_ID = 2
PORT = 5000 + CM_ID
#parameters needed from the CM

INPUTS_CALCULATION_MODULE = [
    {'input_name': 'Pixel threshold',
     'input_type': 'input',
     'input_parameter_name': 'pix_threshold',
     'input_value': 1,
     'input_unit': 'none',
     'input_min': 1,
     'input_max': 10, 'cm_id': CM_ID
     },
    {'input_name': 'District Heating threshold',
     'input_type': 'input',
     'input_parameter_name': 'dh_threshold',
     'input_value': 1,
     'input_unit': 'none',
     'input_min': 1,
     'input_max': 10, 'cm_id': CM_ID
     },

]


SIGNATURE = {
    "category": "Buildings",
    "cm_name": CM_NAME,
    "layers_needed": [
        "heat_density_tot"
    ],
    "cm_url": "Do not add something here",
    "cm_description": "this computation module allows to divide the HDM",
    "cm_id": CM_ID,
    'inputs_calculation_module': INPUTS_CALCULATION_MODULE
}
