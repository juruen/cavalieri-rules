PROJECT(rules)

CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

SET(RULES_SRCS
    ${CMAKE_SOURCE_DIR}/rules.cpp
  )

ADD_DEFINITIONS( -Wall -std=c++11 -g )

INCLUDE_DIRECTORIES(
    ${CMAKE_CURRENT_BINARY_DIR}
    ${CMAKE_BINARY_DIR}
    ${CMAKE_SOURCE_DIR}
    /usr/include/cavalieri
  )

add_library(rules SHARED ${RULES_SRCS})
