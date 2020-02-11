import xgboost as xgb
import matplotlib.pyplot as plt

test_data_name = "agaricus.txt.test"
xgb_test = xgb.DMatrix(test_data_name)
bst = xgb.Booster()
bst.load_model('1.model')
pred = bst.predict(xgb_test)
print(pred)

bst.dump_model("dump.raw.txt")
bst.dump_model("dump.nice.txt", "featmap.txt")


