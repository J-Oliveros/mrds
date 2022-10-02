#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
import pickle
import numpy as np
import boto3
import tempfile


# In[ ]:


def load_csv_from_s3(s3, bucket, filepath, X_csv_file, y_csv_file):
    X_key = filepath + X_csv_file
    y_key = filepath + y_csv_file
    tmp_path = '/tmp/'
    X_tmp = tmp_path + X_csv_file
    y_tmp = tmp_path + y_csv_file

    s3.meta.client.download_file(bucket, X_key, X_tmp)
    s3.meta.client.download_file(bucket, y_key, y_tmp)

    X = np.loadtxt(X_tmp, delimiter=',')
    y = np.loadtxt(y_tmp, delimiter=',')
    return (X, y)


# In[ ]:


def main(event):
    s3 = boto3.resource('s3')
    # bucket = 'nb-scripts'
    # model_key = 'models/commod_classifier.pkl'
    # model_filename = 'commod_classifier.pkl'
    # key_path = 'csv_data/'
    # X_filepath = 'commod_X.csv'
    # y_filepath = 'commod_labels.csv'
    bucket = event['bucket']
    model_key = event['model_key']
    model_filename = event['model_filename']
    key_path = event['key_path']
    X_filepath = event['X_filepath']
    y_filepath = event['y_filepath']
    model = event['model']
    X, y = load_csv_from_s3(s3, bucket, key_path, X_filepath, y_filepath)
    # train
    model.fit(X, y)
    # save model to s3
    with tempfile.TemporaryFile() as f:
        pickle.dump(model, f)
        f.seek(0)
        s3.meta.client.upload_file(f, bucket, model_key)


# In[ ]:


if __name__ == '__main__':
    main(sys.argv[1])

