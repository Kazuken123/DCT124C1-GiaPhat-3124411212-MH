# -*- coding: utf-8 -*-
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# 1. Prepare SGU Banner Image
rgb_img = Image.open('extracted_3.png').convert('RGB')
mask_img = Image.open('extracted_4.png').convert('L')
rgba_img = rgb_img.copy()
rgba_img.putalpha(mask_img)
white_bg = Image.new('RGBA', rgba_img.size, (255, 255, 255, 255))
final_banner = Image.alpha_composite(white_bg, rgba_img).convert('RGB')
final_banner.save('sgu_banner.png', dpi=(300, 300))

plt.rcParams['font.sans-serif'] = ['Segoe UI', 'Arial', 'Tahoma', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 2. Simple Histogram of Tuoi & Boxplot of Luong for Cau 1 - Cau hoi 3
tuoi_valid = [25, 30, 22, 40, 35, 29, 50, 27, 31]
luong_raw = [8000, 5000, 15000, -2000, 7000, 8500, 30000, 8200, 7800]

fig, axes = plt.subplots(1, 2, figsize=(10, 4), dpi=180)

axes[0].hist(tuoi_valid, bins=5, color='#5B9BD5', edgecolor='black')
axes[0].set_title('Histogram của Tuổi', fontsize=11)
axes[0].set_xlabel('Tuổi')
axes[0].set_ylabel('Tần số')
axes[0].grid(axis='y', linestyle='--', alpha=0.5)

axes[1].boxplot(luong_raw, orientation='vertical', widths=0.35)
axes[1].set_title('Boxplot của Lương', fontsize=11)
axes[1].set_ylabel('Lương')
axes[1].set_xticks([1])
axes[1].set_xticklabels(['Lương'])
axes[1].grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('fig_q3_hist_box.png', dpi=180)
plt.close()

# 3. Simple Scatter Plot for Cau 1 - Cau hoi 4
pairs_tuoi = [25, 22, 40, 35, 29, 50, 27, 31]
pairs_luong = [8000, 5000, 15000, -2000, 8500, 30000, 8200, 7800]

fig, ax = plt.subplots(figsize=(6.5, 4), dpi=180)
ax.scatter(pairs_tuoi, pairs_luong, color='#2E75B6', s=45)
ax.set_title('Scatter plot giữa Tuổi và Lương', fontsize=11)
ax.set_xlabel('Tuổi')
ax.set_ylabel('Lương')
ax.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('fig_q4_scatter.png', dpi=180)
plt.close()

# 4. Simple Boxplot for Cau 2c
age_c2 = [13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25, 30, 33, 33, 35, 35, 35, 35, 36, 40, 45, 46, 52, 70]

fig, ax = plt.subplots(figsize=(6.5, 3.2), dpi=180)
ax.boxplot(age_c2, orientation='horizontal', widths=0.4)
ax.set_title('Biểu đồ hộp Boxplot của tập dữ liệu Tuổi', fontsize=11)
ax.set_xlabel('Tuổi')
ax.set_yticks([1])
ax.set_yticklabels(['Tuổi'])
ax.grid(axis='x', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('fig_cau2_boxplot.png', dpi=180)
plt.close()
print("All simple charts generated.")
