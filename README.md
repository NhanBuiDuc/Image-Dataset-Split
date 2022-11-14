# Image-Dataset-Split
To use:<br />
(1) Put your dataset folder in main working directory<br />
(2) The dataset must be in format:<br />
Dataset: <br />----- Class1 ----- Label<br />
        ----- Class2 ----- Label<br />
        ----- Class3 ----- Label<br />
(3) Run: python process.py --data_path Dataset --test_data_path_to_save Dataset/test --train_ratio 0.7<br /><br />
--data_path: path to your dataset directory<br />
--test_data_path_to_save: to specify the folder you want to save the test files<br />
--train_ratio: Train ratio - 0.7 means splitting data in 70 % train and 30 % test<br />
