################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../src/mystring.c \
../src/mystring_ptest.c 

C_DEPS += \
./src/mystring.d \
./src/mystring_ptest.d 

OBJS += \
./src/mystring.o \
./src/mystring_ptest.o 


# Each subdirectory must supply rules for building sources it contributes
src/%.o: ../src/%.c src/subdir.mk
	@echo 'Building file: $<'
	@echo 'Invoking: GCC C Compiler'
	gcc -O3 -Wall -c -fmessage-length=0 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


clean: clean-src

clean-src:
	-$(RM) ./src/mystring.d ./src/mystring.o ./src/mystring_ptest.d ./src/mystring_ptest.o

.PHONY: clean-src

