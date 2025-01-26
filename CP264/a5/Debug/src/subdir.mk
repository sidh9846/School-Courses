################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../src/bigint.c \
../src/bigint_ptest.c \
../src/dllist.c \
../src/myrecord_sllist.c 

C_DEPS += \
./src/bigint.d \
./src/bigint_ptest.d \
./src/dllist.d \
./src/myrecord_sllist.d 

OBJS += \
./src/bigint.o \
./src/bigint_ptest.o \
./src/dllist.o \
./src/myrecord_sllist.o 


# Each subdirectory must supply rules for building sources it contributes
src/%.o: ../src/%.c src/subdir.mk
	@echo 'Building file: $<'
	@echo 'Invoking: GCC C Compiler'
	gcc -O0 -g3 -Wall -c -fmessage-length=0 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


clean: clean-src

clean-src:
	-$(RM) ./src/bigint.d ./src/bigint.o ./src/bigint_ptest.d ./src/bigint_ptest.o ./src/dllist.d ./src/dllist.o ./src/myrecord_sllist.d ./src/myrecord_sllist.o

.PHONY: clean-src

