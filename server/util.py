import json
import pickle
import numpy as np



location = None
model = None
data_column = None

def load_model():
    global location
    global model
    global data_column
    
    with open("./model/banglore_prediction_columns","r") as f:
        data_column = json.load(f)["data_columns"]
        data_column.remove("price")
        location = data_column[9:]
    with open("./model/banglore_predicition_mode.pickle2","rb") as f:
        model = pickle.load(f)
    print("loading models done...")
        
def get_location():
    return location


def predict(size,total_sqft,bath,balcony,area_type,location):
    try:
        #print(data_column)
        
        arr = np.zeros(len(data_column), dtype = float)
        loc =  data_column.index(location.lower())

        d={
            "BuiltupArea":4,
            "CarpetArea":5,
            "PlotArea":6,
            "SuperbuiltupArea":7
        }
        #print(arr)
        #print(loc)
        if loc>7:
            arr[loc] = 1
        arr[d[area_type]] = 1
        arr[0] = size
        arr[1] = total_sqft
        arr[2] = bath
        arr[3] = balcony
        
        pv = model.predict([arr])[0]

        return pv
    except Exception as e:
        print("some error in predicting ->",e)
    
load_model() 
# if __name__ == "__main__":
#     load_model()
#     #print(data_column)
#     #print(len(data_column))
#     #print(location)
#     print(predict(2,1200,3,1,"BuiltupArea","1st Block Jayanagar"))
#     print(predict(4,1850,4,2,"BuiltupArea","Anjanapura"))
#     # print(predict(2,1200,3,1,"BuiltupArea","Vittasandra"))
   
