################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../src/factorial.c \
../src/mychar.c \
../src/mymortgage.c \
../src/mymortgage_ptest.c 

C_DEPS += \
./src/factorial.d \
./src/mychar.d \
./src/mymortgage.d \
./src/mymortgage_ptest.d 

OBJS += \
./src/factorial.o \
./src/mychar.o \
./src/mymortgage.o \
./src/mymortgage_ptest.o 


# Each subdirectory must supply rules for building sources it contributes
src/%.o: ../src/%.c src/subdir.mk
	@echo 'Building file: $<'
	@echo 'Invoking: GCC C Compiler'
	gcc -O0 -g3 -Wall -c -fmessage-length=0 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


clean: clean-src

clean-src:
	-$(RM) ./src/factorial.d ./src/factorial.o ./src/mychar.d ./src/mychar.o ./src/mymortgage.d ./src/mymortgage.o ./src/mymortgage_ptest.d ./src/mymortgage_ptest.o

.PHONY: clean-src

