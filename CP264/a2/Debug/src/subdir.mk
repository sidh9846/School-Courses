################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../src/fibonacci.c \
../src/fibonacci_ptest.c \
../src/matrix.c \
../src/polynomial.c 

C_DEPS += \
./src/fibonacci.d \
./src/fibonacci_ptest.d \
./src/matrix.d \
./src/polynomial.d 

OBJS += \
./src/fibonacci.o \
./src/fibonacci_ptest.o \
./src/matrix.o \
./src/polynomial.o 


# Each subdirectory must supply rules for building sources it contributes
src/%.o: ../src/%.c src/subdir.mk
	@echo 'Building file: $<'
	@echo 'Invoking: GCC C Compiler'
	gcc -O0 -g3 -Wall -c -fmessage-length=0 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


clean: clean-src

clean-src:
	-$(RM) ./src/fibonacci.d ./src/fibonacci.o ./src/fibonacci_ptest.d ./src/fibonacci_ptest.o ./src/matrix.d ./src/matrix.o ./src/polynomial.d ./src/polynomial.o

.PHONY: clean-src

