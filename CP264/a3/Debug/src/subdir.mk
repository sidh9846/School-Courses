################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../src/mystring.c \
../src/mystring_ptest.c \
../src/myword.c \
../src/myword_ptest.c 

C_DEPS += \
./src/mystring.d \
./src/mystring_ptest.d \
./src/myword.d \
./src/myword_ptest.d 

OBJS += \
./src/mystring.o \
./src/mystring_ptest.o \
./src/myword.o \
./src/myword_ptest.o 


# Each subdirectory must supply rules for building sources it contributes
src/%.o: ../src/%.c src/subdir.mk
	@echo 'Building file: $<'
	@echo 'Invoking: GCC C Compiler'
	gcc -O0 -g3 -Wall -c -fmessage-length=0 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


clean: clean-src

clean-src:
	-$(RM) ./src/mystring.d ./src/mystring.o ./src/mystring_ptest.d ./src/mystring_ptest.o ./src/myword.d ./src/myword.o ./src/myword_ptest.d ./src/myword_ptest.o

.PHONY: clean-src

