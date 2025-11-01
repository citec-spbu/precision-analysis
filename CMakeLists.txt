cmake_minimum_required(VERSION 3.5)

project(PrecisionAnalysis VERSION 1.0.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_subdirectory(extern/eigen EXCLUDE_FROM_ALL)

add_library(PrecisionAnalysis STATIC
    src/Parser.cpp
)

target_include_directories(PrecisionAnalysis PUBLIC
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
)

target_link_libraries(PrecisionAnalysis PUBLIC Eigen3::Eigen)

add_executable(example_basic examples/basic_demo.cpp)

target_link_libraries(example_basic PRIVATE PrecisionAnalysis)