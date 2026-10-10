from memory import store_mem
from guardrails import validate_inp,validate_op
from local_ans import get_local_ans
from groq_client import gen_res
from groq import APIError,RateLimitError

def main():
    memory = store_mem()

    print("AI/ML STUDY ASSISTANT BOT")
    print("\n")
    print("Topics:Python,Machine Learning,Deep Learning,AI")
    print("\n")
    print("type 'exit' to quit.\n")


    while True:
        que = input("You: ").strip()


        if que.lower()=="exit":
            print("Bot: happy learning! BYE")
            break
        valid,result = validate_inp(que,memory)

        if not valid:
            print(f"Bot: {result}\n")
            continue

        question = result

        prev_ans = memory.check_with_prev_ans(question)

        if prev_ans is not None:
            print(f"Bot [memory]: {prev_ans}\n")

            memory.add_hist(question,prev_ans)
            continue

        answer = get_local_ans(question)
        if answer is not None:
            print(f"Bot [Local]: {answer}")
            memory.add_hist(question,answer)
            continue

        try:
            answer = gen_res(question,memory.get_hist())

            # if not validate_op(answer):
            #     print("Bot: i couldn't validate the response try again")
            #     continue
            print(f"Bot :{answer}\n")
            memory.add_hist(question,answer)

        except RateLimitError:
            print("Bot : rate limit has been exceed ")


        except APIError as e:
            print("api error: ",e)


        except Exception as e:
            print("Error: ",e)


if __name__ == "__main__":
    main()                            
