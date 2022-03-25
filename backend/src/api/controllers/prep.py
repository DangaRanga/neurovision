from .DataHandler import DataHandler

def prepHRT(handler:DataHandler):
    handler.removeFeature("PatientId")
    handler.removeFeature("Species")
    handler.removeInvalidData()
    handler.translateData()
    handler.normalizeData()
    handler.dataset_split(0)
    return handler

def prepIRS(handler:DataHandler):
    pass

def prepHPR(handler:DataHandler):
    pass