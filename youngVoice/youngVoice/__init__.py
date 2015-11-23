from flask import *
from youngVoice import config
import youngVoice.controller.index
import youngVoice.controller.admin
import youngVoice.controller.article
import youngVoice.controller.question
import youngVoice.controller.notice
import youngVoice.controller.utils
import youngVoice.controller.log
import youngVoice.controller.errorHandler

app = Flask(__name__)
app.secret_key = 'youngVoice233'


