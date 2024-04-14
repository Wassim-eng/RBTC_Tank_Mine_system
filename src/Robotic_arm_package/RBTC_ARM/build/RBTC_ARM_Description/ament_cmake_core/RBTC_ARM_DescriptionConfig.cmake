# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_RBTC_ARM_Description_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED RBTC_ARM_Description_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(RBTC_ARM_Description_FOUND FALSE)
  elseif(NOT RBTC_ARM_Description_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(RBTC_ARM_Description_FOUND FALSE)
  endif()
  return()
endif()
set(_RBTC_ARM_Description_CONFIG_INCLUDED TRUE)

# output package information
if(NOT RBTC_ARM_Description_FIND_QUIETLY)
  message(STATUS "Found RBTC_ARM_Description: 0.0.0 (${RBTC_ARM_Description_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'RBTC_ARM_Description' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${RBTC_ARM_Description_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(RBTC_ARM_Description_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${RBTC_ARM_Description_DIR}/${_extra}")
endforeach()
