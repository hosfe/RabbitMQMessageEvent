
'''
Title: RabbitMQMessageEvent
Authors: Felix Hosner - fhosner@computer-coach.ch
Date: 27.12.2023

Description:
Various specific event handlers allow Opsdroid to handle different
events separately. This allows specific actions to be carried out based
on. – cd550

Command - Input:
await self.parse(RabbitMQMessageEvent(message_data)) 

#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
Important developer information:
This script is provided as a module in Opsdroid.
It is deployed as a pip install module in the docker instance.
The source in the development environment is stored in the directory:
./opsdroid/matrix/module

The components of the Docker instance are in this directory:
/home/opsdroid/module/rabbitmq_message_event
– 5645e
'''
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
# Import the modules and components needed for the project – 2a682
from opsdroid.events import Event
import logging

#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
# Configuring logging is on – be17e
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
'''
The RabbitMQ event handler forwards the data from the RabbitMQ queue
'rabbitmq_consumer_client_skill' as an event to the 'skill-
rabbitmq_process_triage'. – be7a7
'''
class RabbitMQMessageEvent(Event):
    def __init__(self, message_data, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.message_data = message_data
        logger.info(f'Instantiate a RabbitMQMessageEvent object with Object ID: {id(self)}. – 28045')

#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
'''
All matrix messages received by the 'Skill-RabbitMQ_Process_Triage' are
forwarded here to the 'Skill-Matrix_Message_Processor' – 1dc52
'''
class MatrixMessageEvent(Event):
    def __init__(self, message_data, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.message_data = message_data
        logger.info(f'MatrixMessageEvent is instantiated with the Object ID {id(self)}. – 690c1')

#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
'''
All SMSup messages received by the 'Skill-RabbitMQ_Process_Triage' are
sent here to the 'Skill-SMSup_Message_Processor – aaf98
'''
class SMSUpMessageEvent(Event):
    def __init__(self, message_data, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.message_data = message_data
        logger.info(f'Instanziere SMSUpMessageEvent mit der Object-ID: {id(self)}. – fcf36')

#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
'''
All email messages received by the 'skill-rabbitmq_process_triage' are
sent here to the 'skill-email_message_processor' – 424c6
'''
class EMailMessageEvent(Event):
    def __init__(self, message_data, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.message_data = message_data
        logger.info(f'Instance an EMailMessageEvent with Object ID: {id(self)}. – 0bca8')
        
