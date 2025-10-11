from platform import platform, machine, processor, system, version, python_implementation
# print(platform.__dict__)

# max_key_length = max(len(key) for key in platform.__dict__.keys())

# for key, value in platform.__dict__.items():
#     print(f"{key.ljust(max_key_length)} : {value}")

print(processor())
print(system())
