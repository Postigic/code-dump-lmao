#include <stdio.h>
#include <stdint.h>

#define MEMORY_SIZE 1024

uint32_t registers[16];
uint8_t memory[MEMORY_SIZE];

typedef enum {
    MOV,
    ADD,
    SUB,
    JMP,
    HALT
} InstructionSet;

void execute(uint8_t *memory, uint32_t *registers) {
    uint32_t pc = 0;

    while (1) {
        uint8_t instruction = memory[pc++];
        switch (instruction) {
            case MOV: {
                uint8_t reg = memory[pc++];
                uint32_t value = memory[pc++] | (memory[pc++] << 8);
                registers[reg] = value;
                break;
            }
            case ADD: {
                uint8_t reg1 = memory[pc++];
                uint8_t reg2 = memory[pc++];
                registers[reg1] += registers[reg2];
                break;
            }
            case SUB: {
                uint8_t reg1 = memory[pc++];
                uint8_t reg2 = memory[pc++];
                registers[reg1] -= registers[reg2];
                break;
            }
            case JMP: {
                pc = memory[pc++];
                break;
            }
            case HALT:
                return;
            default:
                printf("Invalid instruction: 0x%x\n", instruction);
                return;
        }
    }
};

void load_program(uint8_t *memory) {
    memory[0] = MOV; memory[1] = 0; memory[2] = 10; memory[3] = 0;
    memory[4] = MOV; memory[5] = 1; memory[6] = 20; memory[7] = 0;
    memory[8] = ADD; memory[9] = 0; memory[10] = 1;
    memory[11] = HALT;
}

int main() {
    load_program(memory);
    execute(memory, registers);

    for (int i = 0; i < 16; i++) {
        printf("Register %d: %d\n", i, registers[i]);
    }
    
    return 0;
}

