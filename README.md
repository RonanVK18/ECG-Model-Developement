The MIT-BIH Arrhythmia Dataset is a widely used benchmark for evaluating ECG classification algorithms and arrhythmia detection systems. 
The dataset contains 48 half-hour excerpts of two-channel ambulatory ECG recordings, digitized at 360 samples per second with 11-bit resolution over a 10 mV range.

The mitbih_test.csv file typically includes a subset of the 48 records in the MIT-BIH Arrhythmia Dataset. 
The specific records used for testing are often chosen to ensure a balanced representation of different arrhythmia types and to avoid overlap with the training set.

The model the data has been trained on has been resampled to avoid any sort of bias observed in the model due to an unbalanced dataset.

The samples provided are samples extracted for each class from the mitbih_test.csv dataset, this data has been preprocessed and only needs to be fit into the model for appropriate class predictiions.

This directory diretly consists of an inference script as well as a sample dataset(columns not copied).

The preloaded model has been saved as as a ".h5" file and can be preloaded using the latest tensorflow version v2.16.1  using load_model

The Data does not need preprocessing only reshaped to fit the model accurately, that part has been conducted by the "function" in the inference script splits the data into 2 parts X & Y,
allowing us to categorically predict the value of the last column.

Once the categorical value has been predicted it is then compared aagainst an existing dictionary of labels that we have understood from the DATASET.

Test_dat.csv : Each row is individual readings of clients, last row belongs to the 0(Normal) class.
Test_dat.csv : Each row is individual readings of clients, last row belongs to the 1(Atrial Premature) class.
Test_dat.csv : Each row is individual readings of clients, last row belongs to the 2(Premature Ventricular Contraction) class.
Test_dat.csv : Each row is individual readings of clients, last row belongs to the 3(Fusion of Ventricular & Normal) class.
Test_dat.csv : Each row is individual readings of clients, last row belongs to the 4(Fusion of Paced & Normal) class.
