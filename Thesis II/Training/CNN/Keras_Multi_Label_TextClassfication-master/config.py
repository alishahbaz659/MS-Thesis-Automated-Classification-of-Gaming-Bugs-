MODEL_PATH='saves/model.h5'
TOK_PATH='saves/tokenizer.pickle'
LOG_PATH='./logs/fit/'
EMBEDDING_PATH = 'dataset/glove/glove.6B.300d.txt'
TRAIN_PATH='data/train.csv'
PREDICT_PATH='data/train.csv'
PREDICT_LEVEL=0.5
# TRAIN_PATH='data/pre_data.csv'
# PREDICT_PATH='data/pre_data.csv'



CLASSES=['invalidPositionOverTime', 'implementationResponseIssue', 'invalidContextOverTime', 'interruptedEvent', 
                        'invalidEventOccurraceOverTime','actionNotPossible','actionWhenNotAllowed','informationOutOfOrder','lackOfRequiredInformation',
                        'invalidInfoAccess','objectOutOfBoundForAnyState','objectOutOfBoundForSpecificState','artificialStupidity','invalidValueChange',
                        'invalidGraphicalRespresentation']

MAX_SEQUENCE_LEN=256
MAX_WORDS_LEN=20000
EMBED_SIZE=300

CNN='CNN_MODEL'
CHAR_CNN='CHAR_CNN'

FAST='FAST'

TEXT_LSTM='TEXT_LSTM'
TEXT_BI_LSTM='TEXT_BI_LSTM'
TEXT_ATT_BI_LSTM='TEXT_ATT_BI_LSTM'

TEXT_GRU='TEXT_GRU'
TEXT_BI_GRU='TEXT_BI_GRU'
TEXT_ATT_BI_GRU='TEXT_ATT_BI_GRU'

