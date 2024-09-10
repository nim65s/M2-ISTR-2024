cmake_minimum_required(VERSION 3.20)

project(M2-ISTR-2024 LANGUAGES CXX)

add_library(add SHARED include/add.hpp src/add.cpp)
target_include_directories(add PUBLIC include)

add_executable(hello hello.cpp)
target_link_libraries(hello PUBLIC add)
