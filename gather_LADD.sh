cd dataset
# Creating dirs
mkdir full_train_ds
mkdir full_train_ds/Annotations
mkdir full_train_ds/JPEGImages

# Copy images and annotations

cp LADD/spring_korolev_2019/Annotations/* full_train_ds/Annotations/
cp LADD/summer_moscow_2019/Annotations/* full_train_ds/Annotations/
cp LADD/summer_tambov_2019/Annotations/* full_train_ds/Annotations/
cp LADD/winter_moscow_2018/Annotations/* full_train_ds/Annotations/
cp LADD/summer_nnovgorod_2021/Annotations/* full_train_ds/Annotations/
cp LADD/spring_korolev_2019/JPEGImages/* full_train_ds/JPEGImages/
cp LADD/summer_moscow_2019/JPEGImages/* full_train_ds/JPEGImages/
cp LADD/summer_tambov_2019/JPEGImages/* full_train_ds/JPEGImages/
cp LADD/winter_moscow_2018/JPEGImages/* full_train_ds/JPEGImages/
cp LADD/summer_nnovgorod_2021/JPEGImages/* full_train_ds/JPEGImages/

# Merge imageset

mkdir -p full_train_ds/ImageSets/Main

cat LADD/spring_korolev_2019/ImageSets/Main/train.txt \
LADD/summer_moscow_2019/ImageSets/Main/train.txt \
LADD/summer_tambov_2019/ImageSets/Main/train.txt \
LADD/winter_moscow_2018/ImageSets/Main/train.txt \
LADD/summer_nnovgorod_2021/ImageSets/Main/train.txt > full_train_ds/ImageSets/Main/train.txt

cat LADD/spring_korolev_2019/ImageSets/Main/trainval.txt \
LADD/summer_moscow_2019/ImageSets/Main/trainval.txt \
LADD/summer_tambov_2019/ImageSets/Main/trainval.txt \
LADD/winter_moscow_2018/ImageSets/Main/trainval.txt \
LADD/summer_nnovgorod_2021/ImageSets/Main/trainval.txt > full_train_ds/ImageSets/trainval.txt

cat LADD/spring_korolev_2019/ImageSets/Main/val.txt \
LADD/summer_moscow_2019/ImageSets/Main/val.txt \
LADD/summer_tambov_2019/ImageSets/Main/val.txt \
LADD/winter_moscow_2018/ImageSets/Main/val.txt \
LADD/summer_nnovgorod_2021/ImageSets/Main/val.txt > full_train_ds/ImageSets/Main/val.txt

cat LADD/spring_korolev_2019/ImageSets/Main/test.txt \
LADD/summer_moscow_2019/ImageSets/Main/test.txt \
LADD/summer_tambov_2019/ImageSets/Main/test.txt \
LADD/winter_moscow_2018/ImageSets/Main/test.txt \
LADD/summer_nnovgorod_2021/ImageSets/Main/test.txt > full_train_ds/ImageSets/Main/test.txt

cd ..