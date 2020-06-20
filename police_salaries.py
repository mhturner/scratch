import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns
import matplotlib

"""
https://www.kaggle.com/kaggle/sf-salaries
"""

font = {'weight' : 'bold',
        'size'   : 12}

matplotlib.rc('font', **font)

data_dir = '/home/mhturner/Downloads'
fn = 'Salaries.csv'

Sal = pd.read_csv(os.path.join(data_dir, fn))
target_year = 2014
def getFTsalaries(df, job_title_id, target_year=2014):
    FTSal = df[np.logical_and(df.JobTitle.str.contains(job_title_id, case=False), Sal.Status=='FT')]
    salaries = np.array([np.float(x) for x in FTSal[FTSal.Year==target_year].TotalPayBenefits])
    return salaries

colors = sns.color_palette("Set2")

fh, ax = plt.subplots(2, 1, figsize=(12,12))

all_salaries = getFTsalaries(Sal, '', target_year=target_year)
val_all, bin_all = np.histogram(all_salaries, 50, density=True)
ax[0].plot(bin_all[:-1], val_all, alpha=1, LineWidth=2, color='k', label='All county employees')

sfpd_salaries = getFTsalaries(Sal, 'POLICE', target_year=target_year)
val_sfpd, bin_sfpd = np.histogram(sfpd_salaries, 50, density=True)
ax[0].plot(bin_sfpd[:-1], val_sfpd, color=colors[0], LineWidth=2, label='SFPD')

sheriff_salaries = getFTsalaries(Sal, 'SHERIFF', target_year=target_year)
val_sheriff, bin_sheriff = np.histogram(sheriff_salaries, 50, density=True)
ax[0].plot(bin_sheriff[:-1], val_sheriff, color=colors[1], LineWidth=2, label='Sheriff')

# transit_salaries = getFTsalaries(Sal, 'TRANSIT', target_year=target_year)
# val_transit, bin_transit = np.histogram(transit_salaries, 50, density=True)
# ax[0].plot(bin_transit[:-1], val_transit, color=colors[2], LineWidth=2, label='Transit')

ax[0].set_xlabel('{} Total pay + benefits ($)'.format(target_year))
ax[0].set_ylabel('Fraction of employees')
ax[0].set_yticks([])
ax[0].set_xticks(np.arange(50000, 500000, 50000))
ax[0].get_xaxis().set_major_formatter(
     mtick.FuncFormatter(lambda x, p: format(int(x), ',')))

fh.legend(loc=(1, 1), bbox_to_anchor=(0.5,0.7), fancybox=True)


titles = ['Police', 'Sheriff', 'Transit', 'Custodian', 'Fire', 'Electrician', 'Engineer', 'Laborer', 'Librarian', 'Social Worker', 'Clerk']

medians = []
for t_ind, title in enumerate(titles):
    median = np.median(getFTsalaries(Sal, title, target_year=target_year))
    medians.append(median)

s_inds = np.argsort(medians)

medians = np.array(medians)[s_inds]
titles = np.array(titles)[s_inds]

ax[1].bar(np.arange(0,len(medians)), medians, tick_label=np.array(titles), width=0.5)
ax[1].set_ylabel('Median pay + benefits ($)')
plt.xticks(rotation='vertical')

ax[1].get_yaxis().set_major_formatter(
     mtick.FuncFormatter(lambda x, p: format(int(x), ',')))

fh.savefig(os.path.join(data_dir, 'SF_countypay_{}.png'.format(target_year)))

# %%
Sal['JobTitle'].value_counts()[:80].index.tolist()
