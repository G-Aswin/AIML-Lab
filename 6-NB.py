import numpy as np
import pandas as pd
data = pd.DataFrame()
data['Gender'] = ['male','male','male','male','female','female','female','female']
data['Height'] = [6,5.92,5.58,5.92,5,5.5,5.42,5.75]
data['Weight'] = [180,190,170,165,100,150,130,150]
data['Foot_Size'] = [12,11,12,10,6,8,7,9]
print("\n Dataset")
print("")
print(data)


person = pd.DataFrame()
person['Height'] = [5]
person['Weight'] = [130]
person['Foot_Size'] = [6]
print('\n Test Instance: ')
print(" ")
print(person)


n_male = data['Gender'][data['Gender'] == 'male'].count()
n_female = data['Gender'][data['Gender'] == 'female'].count()
total_ppl = data['Gender'].count()
 
p_male = n_male / total_ppl     #(4/8)
p_female = n_female / total_ppl     #(4/8)

data_means = data.groupby('Gender').mean() 
print('\n Dataset Mean')
print(" ")
print(data_means)
data_variance = data.groupby('Gender').var()
print(data_variance)

male_height_mean = data_means['Height']['male']
male_weight_mean = data_means['Weight']['male']
male_footsize_mean  = data_means['Foot_Size']['male']
print("male_height_mean: ", male_height_mean)
print("male_weight_mean: ", male_weight_mean)
print("male_footsize_mean: ", male_footsize_mean)

male_height_variance = data_variance['Height']['male'] 
male_weight_variance = data_variance['Weight']['male']
male_footsize_variance = data_variance['Foot_Size']['male']
print("male_height_variance: ",male_height_variance)
print("male_weight_variance: ",male_weight_variance)
print("male_footsize_variance: ",male_footsize_variance)
 
female_height_mean = data_means['Height'][data_means.index == 'female'].values[0]
female_height_mean = data_means['Height']['female']



female_weight_mean = data_means['Weight']['female']
female_footsize_mean  = data_means['Foot_Size']['female']
print("female_height_mean: ", female_height_mean)
print("female_weight_mean: ", female_weight_mean)
print("female_footsize_mean: ", female_footsize_mean)

female_height_variance = data_variance['Height']['female']
female_weight_variance = data_variance['Weight']['female']
female_footsize_variance = data_variance['Foot_Size']['female']
print("female_height_variance: ",female_height_variance)
print("female_weight_variance: ",female_weight_variance)
print("female_footsize_variance: ",female_footsize_variance)


def p_x_given_y(x,mean_y, variance_y):
    p = 1/(np.sqrt(2*np.pi*variance_y))* np.exp((-(x-mean_y) ** 2)/(2*variance_y))
    return p


print('\n Probability male: ')
prob_male = p_male*p_x_given_y(person['Height'][0],data_means['Height']['male'],male_height_variance)* p_x_given_y(person['Weight'][0],male_weight_mean,male_weight_variance)* p_x_given_y(person['Foot_Size'][0],male_footsize_mean,male_footsize_variance)
print(prob_male)

print('\n Probability female: ')
prob_female = p_female*p_x_given_y(person['Height'][0],female_height_mean,female_height_variance)* p_x_given_y(person['Weight'][0],female_weight_mean,female_weight_variance)* p_x_given_y(person['Foot_Size'][0],female_footsize_mean,female_footsize_variance)
print(prob_female)

if(prob_male > prob_female):
    print("target label: Male")
else:
    print("target label: Female")
 