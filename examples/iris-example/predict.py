from igel import IgelModel


"""
The goal of igel is to use ML without writing code. Therefore, the right and simplest way to use igel is from terminal.
You can run ` igel predict -dp path_to_dataset`.

Alternatively, you can write code if you want. This example below demonstrates how to use igel if you want to write code.

"""

mock_pred_params = {'data_path': '../data/iris/test-Iris.csv',
                    'cmd': 'predict'}

IgelModel(**mock_pred_params).predict()
