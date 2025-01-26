"""
-------------------------------------------------------
Assignment 3, Task 6
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2023-02-05"
-------------------------------------------------------
"""

from functions import is_mirror_stack

mirror = is_mirror_stack("cmc", "abc", "m")
print(f"Mirror: {mirror.value}")

mirror = is_mirror_stack("zzxzuzxzz", "xyz", "u")
print(f"Mirror: {mirror.value}")

mirror = is_mirror_stack("cmc", "ab", "m")
print(f"Mirror: {mirror.value}")

mirror = is_mirror_stack("zzxzxzxzz", "xyz", "u")
print(f"Mirror: {mirror.value}")

mirror = is_mirror_stack("zzxzuzx", "xyz", "u")
print(f"Mirror: {mirror.value}")

mirror = is_mirror_stack("cmc", "abc", "m")
print(f"Mirror: {mirror.value}")

mirror = is_mirror_stack("acmcb", "abc", "m")
print(f"Mirror: {mirror.value}")
