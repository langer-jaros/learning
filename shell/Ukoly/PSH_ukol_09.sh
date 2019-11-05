# Jaroslav Langer 
# 24/04/2019

#1      
sed 'w jmena' jmena1 jmena2

#2
sed '1~3i a)' input | sed '/a)/{N; s/\n/ /}' | sed '2~3i b)' | sed '/b)/{N; s/\n/ /}' | sed '3~3i c)' | sed '/c)/{N; s/\n/ /}'

#3
sed -e '{s/<\/.*>//; s/<.*>//; /^[[:blank:]]*$/d}' /scratch/expressions/index.html

#4
egrep '^s' /etc/group | awk -F : '{print $3, $1}'

#5
awk -F , '{print $1 " - " $2 " = " $1-$2 }' input