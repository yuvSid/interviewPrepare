cmake_minimum_required(VERSION 3.12)

# specify the C++ standard
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# specify where to find boost
# list(APPEND CMAKE_MODULE_PATH "/home/repos/libraries/boost_1_80_0")

# set the project name
project(leetcode)

# Find Boost headers only:
find_package(Boost 1.80.0)
if(Boost_FOUND)
    # add the executable
    add_executable(leetcode "cplusplus/main.cpp")
    target_include_directories(leetcode PUBLIC
                          "${PROJECT_SOURCE_DIR}/cplusplus"
                          "${Boost_INCLUDE_DIRS}"
                          )
endif()




