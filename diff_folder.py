import filecmp
import difflib
import os


class FolderComparator:
    def __init__(self, folder1, folder2):
        self.folder1 = folder1
        self.folder2 = folder2

    def compare_folders(self):
        dir_comparison = filecmp.dircmp(self.folder1, self.folder2)
        self._print_diff_files(dir_comparison)
        self._compare_subfolders(dir_comparison)

    def _print_diff_files(self, dir_comparison):
        for file_name in dir_comparison.diff_files:
            print('###############################################')
            print(file_name)
            print(f"存在差异文件: {file_name}")
            print(file_name)
            self._print_file_diff_content(file_name)

        for file_name in dir_comparison.left_only:
            print(f"只存在 {self.folder1} 单个目录文件: {file_name}")

        for file_name in dir_comparison.right_only:
            print(f"只存在 {self.folder2} 单个目录文件: {file_name}")

    def _compare_subfolders(self, dir_comparison):
        for common_dir in dir_comparison.common_dirs:
            subfolder1 = os.path.join(self.folder1, common_dir)
            subfolder2 = os.path.join(self.folder2, common_dir)
            print("##################################")
            print(subfolder1)
            print(subfolder2)
            bak1 = self.folder1
            bak2 = self.folder2
            self.folder1 = subfolder1
            self.folder2 = subfolder2
            print("##################################")
            # if not (os.path.exists(subfolder1) and os.path.exists(subfolder2)):
            #     return
            subfolder_comparison = filecmp.dircmp(subfolder1, subfolder2)
            print(subfolder_comparison.diff_files)
            self._print_diff_files(subfolder_comparison)
            self._compare_subfolders(subfolder_comparison)
            self.folder1 = bak1
            self.folder2 = bak2

    def _print_file_diff_content(self, file_name):
        file_path1 = os.path.join(self.folder1, file_name)
        file_path2 = os.path.join(self.folder2, file_name)
        try:
            with open(file_path1, "r") as file1, open(file_path2, "r") as file2:
                diff = difflib.unified_diff(
                    file1.readlines(),
                    file2.readlines(),
                    fromfile=f"{self.folder1}/{file_name}",
                    tofile=f"{self.folder2}/{file_name}",
                )
                print("\n".join(diff))
        except Exception as e:
            print(e)

# class FolderComparator:
#     def __init__(self, folder1, folder2):
#         self.folder1 = folder1
#         self.folder2 = folder2

#     def compare_folders(self):
#         dir_comparison = filecmp.dircmp(self.folder1, self.folder2)
#         parent_dir1 = self.folder1
#         parent_dir2 = self.folder2
#         self._print_diff_files(dir_comparison, parent_dir1, parent_dir2)
#         self._compare_subfolders(dir_comparison, parent_dir1, parent_dir2)

#     def _print_diff_files(self, dir_comparison, parent_dir1, parent_dir2):
#         for file_name in dir_comparison.diff_files:
#             print('###############################################')
#             print(file_name)
#             print(f"存在差异文件: {file_name}")
#             print(file_name)
#             self._print_file_diff_content(file_name, parent_dir1, parent_dir2)

#         for file_name in dir_comparison.left_only:
#             print(f"只存在 {self.folder1} 单个目录文件: {file_name}")

#         for file_name in dir_comparison.right_only:
#             print(f"只存在 {self.folder2} 单个目录文件: {file_name}")

#     def _compare_subfolders(self, dir_comparison, parent_dir1, parent_dir2):
#         for common_dir in dir_comparison.common_dirs:
#             subfolder1 = os.path.join(parent_dir1, common_dir)
#             subfolder2 = os.path.join(parent_dir2, common_dir)
#             print("##################################")
#             print(subfolder1)
#             print(subfolder2)
#             print("##################################")
#             # if not (os.path.exists(subfolder1) and os.path.exists(subfolder2)):
#             #     return
#             subfolder_comparison = filecmp.dircmp(subfolder1, subfolder2)
#             print(subfolder_comparison.diff_files)
#             self._print_diff_files(subfolder_comparison, subfolder1, subfolder2)
#             self._compare_subfolders(subfolder_comparison, subfolder1, subfolder2)

#     def _print_file_diff_content(self, file_name, parent_dir1, parent_dir2):
#         file_path1 = os.path.join(parent_dir1, file_name)
#         file_path2 = os.path.join(parent_dir2, file_name)
#         with open(file_path1, "r") as file1, open(file_path2, "r") as file2:
#             diff = difflib.unified_diff(
#                 file1.readlines(),
#                 file2.readlines(),
#                 fromfile=f"{self.folder1}/{file_name}",
#                 tofile=f"{self.folder2}/{file_name}",
#             )
#             print("\n".join(diff))
dir1 = "E:\\diff\\folder1"
dir2 = "E:\\diff\\folder2"

comparator = FolderComparator(dir1, dir2)
comparator.compare_folders()