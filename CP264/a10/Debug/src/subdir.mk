################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../src/algorithm.c \
../src/algorithm_ptest.c \
../src/edgelist.c \
../src/graph.c \
../src/heap.c \
../src/queue_stack.c 

C_DEPS += \
./src/algorithm.d \
./src/algorithm_ptest.d \
./src/edgelist.d \
./src/graph.d \
./src/heap.d \
./src/queue_stack.d 

OBJS += \
./src/algorithm.o \
./src/algorithm_ptest.o \
./src/edgelist.o \
./src/graph.o \
./src/heap.o \
./src/queue_stack.o 


# Each subdirectory must supply rules for building sources it contributes
src/%.o: ../src/%.c src/subdir.mk
	@echo 'Building file: $<'
	@echo 'Invoking: GCC C Compiler'
	gcc -O0 -g3 -Wall -c -fmessage-length=0 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


clean: clean-src

clean-src:
	-$(RM) ./src/algorithm.d ./src/algorithm.o ./src/algorithm_ptest.d ./src/algorithm_ptest.o ./src/edgelist.d ./src/edgelist.o ./src/graph.d ./src/graph.o ./src/heap.d ./src/heap.o ./src/queue_stack.d ./src/queue_stack.o

.PHONY: clean-src

