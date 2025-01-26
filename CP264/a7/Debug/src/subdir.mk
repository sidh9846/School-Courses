################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../src/bst.c \
../src/myrecord_bst.c \
../src/queue_stack.c \
../src/tree.c \
../src/tree_ptest.c 

C_DEPS += \
./src/bst.d \
./src/myrecord_bst.d \
./src/queue_stack.d \
./src/tree.d \
./src/tree_ptest.d 

OBJS += \
./src/bst.o \
./src/myrecord_bst.o \
./src/queue_stack.o \
./src/tree.o \
./src/tree_ptest.o 


# Each subdirectory must supply rules for building sources it contributes
src/%.o: ../src/%.c src/subdir.mk
	@echo 'Building file: $<'
	@echo 'Invoking: GCC C Compiler'
	gcc -O0 -g3 -Wall -c -fmessage-length=0 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


clean: clean-src

clean-src:
	-$(RM) ./src/bst.d ./src/bst.o ./src/myrecord_bst.d ./src/myrecord_bst.o ./src/queue_stack.d ./src/queue_stack.o ./src/tree.d ./src/tree.o ./src/tree_ptest.d ./src/tree_ptest.o

.PHONY: clean-src

