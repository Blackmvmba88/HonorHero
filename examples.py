"""
Example usage and demonstration of HonorHero
"""

from honorhero import HonorHero
import time


def simple_example():
    """Simple example of using HonorHero"""
    
    print("Simple HonorHero Example")
    print("=" * 50)
    
    # Create engine
    engine = HonorHero()
    
    # Define update callback
    def on_update(metrics):
        score = metrics.get('honor_score', 0)
        tier = metrics.get('tier', 'N/A')
        print(f"Current Score: {score:.1f} - {tier}")
    
    # Start performance evaluation
    engine.start_performance(on_update)
    
    # Let it run for 10 seconds
    print("Evaluating for 10 seconds...")
    time.sleep(10)
    
    # Stop and get results
    results = engine.stop_performance()
    
    print("\nFinal Results:")
    print(f"Honor Score: {results['final_honor_score']:.1f}")
    print(f"Tier: {results['tier']}")
    print(f"Message: {results['message']}")
    print("\nComponents:")
    for component, score in results['components'].items():
        print(f"  {component}: {score:.1f}")


def programmatic_example():
    """Example of using HonorHero programmatically"""
    
    print("\nProgrammatic HonorHero Example")
    print("=" * 50)
    
    engine = HonorHero()
    
    # Start performance
    engine.start_performance()
    
    # Simulate a performance session
    for i in range(5):
        time.sleep(2)
        status = engine.get_current_status()
        if status:
            print(f"Update {i+1}: Score = {status.get('honor_score', 0):.1f}")
    
    # Stop and get final results
    results = engine.stop_performance()
    
    print(f"\nFinal Honor Score: {results['final_honor_score']:.1f}")
    print(f"Tier: {results['tier']}")
    print(f"Progress: {results['progress']}")


if __name__ == '__main__':
    print("HonorHero Examples")
    print("=" * 50)
    print("\n1. Simple example with callback")
    print("2. Programmatic example")
    print("\nChoose an example (or Ctrl+C to exit):")
    
    try:
        choice = input("> ")
        if choice == "1":
            simple_example()
        elif choice == "2":
            programmatic_example()
        else:
            print("Invalid choice")
    except KeyboardInterrupt:
        print("\nExiting...")
