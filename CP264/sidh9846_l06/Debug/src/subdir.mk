################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../src/data.c \
../src/data2.c \
../src/main.c \
../src/main2.c \
../src/queue_linked.c \
../src/stack_linked.c 

C_DEPS += \
./src/data.d \
./src/data2.d \
./src/main.d \
./src/main2.d \
./src/queue_linked.d \
./src/stack_linked.d 

OBJS += \
./src/data.o \
./src/data2.o \
./src/main.o \
./src/main2.o \
./src/queue_linked.o \
./src/stack_linked.o 


# Each subdirectory must supply rules for building sources it contributes
src/%.o: ../src/%.c src/subdir.mk
	@echo 'Building file: $<'
	@echo 'Invoking: GCC C Compiler'
	gcc -O0 -g3 -Wall -c -fmessage-length=0 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


clean: clean-src

clean-src:
	-$(RM) ./src/data.d ./src/data.o ./src/data2.d ./src/data2.o ./src/main.d ./src/main.o ./src/main2.d ./src/main2.o ./src/queue_linked.d ./src/queue_linked.o ./src/stack_linked.d ./src/stack_linked.o

.PHONY: clean-src

