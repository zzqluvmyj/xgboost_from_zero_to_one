import xgboost as xgb

import matplotlib.pyplot as plt

train_data_name = "agaricus.txt.train"
xgb_train = xgb.DMatrix(train_data_name)
test_data_name = "agaricus.txt.test"
xgb_test = xgb.DMatrix(test_data_name)

params = {
    "objective": "binary:logistic",
    "booster": "gbtree",
    "eta": 1.0,
    "gamma": 1.0,
    "min_child_weight": 1,
    "max_depth": 3
}

num_round = 4
watchlist = [(xgb_train, 'train'), (xgb_test, 'test')]

model = xgb.train(params, xgb_train, num_round, watchlist)
model.save_model("./1.model")

pred = model.predict(xgb_test)
print(pred)

# plt.rcParams['savefig.dpi'] = 300  # 图片像素
# # plt.rcParams['figure.dpi'] = 300  # 分辨率
# # xgb.plot_tree(model, fmap='featmap.txt', num_trees=1)
# # plt.show()
