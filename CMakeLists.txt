cmake_minimum_required(VERSION 3.12)

# specify the C++ standard
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# set the project name
project(leetcode)

# add the executable
add_executable(leetcode "cplusplus/main.cpp")

target_include_directories(leetcode PUBLIC
                          "${PROJECT_SOURCE_DIR}/cplusplus"
                          )

